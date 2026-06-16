<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    foreach ($_POST as $key => $value) {
        if (is_array($value)) {
            echo "<strong>$key:</strong><br>";
            foreach ($value as $item) {
                echo "- " . htmlspecialchars($item) . "<br>";
            }
        } else {
            echo "<strong>$key:</strong> " . htmlspecialchars($value) . "<br>";
        }
    }
} else {
    echo "No data submitted.";
}
?>
