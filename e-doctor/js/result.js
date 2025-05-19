// Retrieve form data from localStorage
const formData = JSON.parse(localStorage.getItem("consultationData"));

// Display the result
if (formData) {
  const resultDisplay = document.getElementById("resultDisplay");
  resultDisplay.innerHTML = `
    <p><strong>First Name:</strong> ${formData.firstName}</p>
    <p><strong>Contact Number:</strong> ${formData.contactNumber}</p>
    <p><strong>Village:</strong> ${formData.village}</p>
    <p><strong>Email:</strong> ${formData.email}</p>
    <p><strong>Issue:</strong> ${formData.issue}</p>
  `;
} else {
  // If no data is found, show an error message
  const resultDisplay = document.getElementById("resultDisplay");
  resultDisplay.innerHTML = "<p>No consultation data found.</p>";
}
