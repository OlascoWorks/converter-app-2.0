function deleteConversion(conversionId) {
    fetch('/delete-conversion', {
        method: 'POST',
        body: JSON.stringify({ conversionId: conversionId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}