const textField = document.querySelector('input[type="text"]');
const submitButton = document.querySelector('button[type="submit"]');

submitButton.addEventListener('click', async () => {
  const textValue = textField.value;
  const base64Text = btoa(textValue);
  const apiUrl = `http://127.0.0.1:5000/api/${base64Text}`;
  const response = await fetch(apiUrl);

  if (response.ok) {
    console.log('Request successful');
  } else {
    console.error('Request failed');
  }
});
function btoa(str) {
  return Buffer.from(str).toString('base64');
}