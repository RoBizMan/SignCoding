document.addEventListener("DOMContentLoaded", function () {
    // Get the public key and client secret from the HTML
    const stripePublicKey = JSON.parse(document.getElementById("id_stripe_public_key").textContent);
    const clientSecret = JSON.parse(document.getElementById("id_client_secret").textContent);
    
    const stripe = Stripe(stripePublicKey); // Initialize Stripe with public key
    const elements = stripe.elements(); // Initialize Stripe Elements
    const cardElement = elements.create("card");
    cardElement.mount("#card-element");

    // Get references to the DOM elements
    const submitButton = document.getElementById("submit-button");
    const cardErrors = document.getElementById("card-errors");

    // Reset the submit button to be clickable after any error
    function resetSubmitButton() {
        submitButton.disabled = false;
        submitButton.classList.remove("disabled");
    }

    if (submitButton) {
        submitButton.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent default button click behavior

            // Validate form fields
            let isValid = true;

            const sessionDate = document.getElementById("hidden-session-date").value;
            if (!sessionDate) {
                document.getElementById("date-error").textContent = "Please select a session date.";
                isValid = false;
            }

            const selectedSlots = document.getElementById("time-slots").value;
            if (!selectedSlots || selectedSlots.length === 0) {
                document.getElementById("time-slots-error").textContent = "Please select at least one time slot.";
                isValid = false;
            }

            // Proceed with payment confirmation if everything is valid
            if (isValid) {
                const bookingId = document.getElementById("booking-id").value; // Get booking ID from hidden input

                // Use Stripe to validate the card element
                stripe.createPaymentMethod({
                    type: 'card',
                    card: cardElement,
                }).then(function(result) {
                    if (result.error) {
                        cardErrors.textContent = result.error.message;
                        resetSubmitButton(); // Re-enable button on error
                    } else {
                        // Proceed with payment confirmation using client secret
                        stripe.confirmCardPayment(clientSecret, {
                            payment_method: result.paymentMethod.id,
                        }).then(function (result) {
                            if (result.error) {
                                cardErrors.textContent = result.error.message;
                                resetSubmitButton(); // Re-enable button on error
                            } else {
                                if (result.paymentIntent.status === "succeeded") {
                                    // Redirect to success page using bookingId from hidden input
                                    const successUrl = `/bookings/booking-success/${bookingId}/`; 
                                    window.location.href = successUrl;
                                }
                            }
                        }).catch(function (error) {
                            cardErrors.textContent = "An error occurred: " + error.message;
                            resetSubmitButton(); // Re-enable button on catch error
                        });
                    }
                });
            }
        });
    } else {
        console.error("Submit button not found!");
    }
});
