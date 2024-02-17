<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Function to construct a string with selected options
    function constructString($label, $value) {
        return "<p>$label: $value</p>";
    }

    // Retrieve form data
    $subject = $_POST["subject"];
    $grade = $_POST["grade"];
    $topic = $_POST["text-input"];
    $checkboxes = $_POST["checkboxes"];

    // Construct the string
    $resultString = constructString("Subject", $subject);
    $resultString .= constructString("Grade", $grade);
    $resultString .= constructString("Topic", $topic);

    if (!empty($checkboxes)) {
        $resultString .= "<p>Selected checkboxes:</p>";
        foreach ($checkboxes as $checkbox) {
            $resultString .= "<p>- $checkbox</p>";
        }
    }

    // Output the result
    echo "<h2>Form Submission Result</h2>";
    echo $resultString;
} else {
    echo "<p>No data submitted.</p>";
}
?>
