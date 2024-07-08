while loop for autocracy

    function ensureCheckboxIsChecked() {
        const checkbox = document.getElementById('the-checkbox');
        if (!checkbox.checked) {
            checkbox.checked = true;
        }
    }
    setInterval(ensureCheckboxIsChecked, 100);
