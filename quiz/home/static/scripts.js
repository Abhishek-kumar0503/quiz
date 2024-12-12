
document.querySelector('form').addEventListener('submit', function(event) {
    const selectedOption = document.querySelector('input[name="selected_option"]:checked');
    if (!selectedOption) {
        alert('Please select an option before submitting.');
        event.preventDefault();
    }
});
