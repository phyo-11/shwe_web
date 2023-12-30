
function updateDimensionAndCalculate(imageIndex) {
    var selectedDimension = document.getElementById("dimensionSelector_" + imageIndex).value;
    var originalWidth = parseFloat(document.getElementById("imageWidth_" + imageIndex).getAttribute("data-original-width"));
    var originalHeight = parseFloat(document.getElementById("imageWidth_" + imageIndex).getAttribute("data-original-height"));
    var calculatedDimension = calculateDimension(originalWidth, originalHeight, selectedDimension);
    document.getElementById("imageWidth_" + imageIndex).innerText = "Width(Picture): " + calculatedDimension.calculatedWidth + " " + selectedDimension;
    document.getElementById("imageHeight_" + imageIndex).innerText = "Height(Picture): " + calculatedDimension.calculatedHeight + " " + selectedDimension;
}

function calculateDimension(originalWidth, originalHeight, selectedDimension) {
    console.log(originalHeight, originalWidth)
    var coversionRate;

    switch (selectedDimension) {
        case 'Inch':
            coversionRate = 1;
            break;

        case 'Centimeter':
            coversionRate = 2.54;
            break;
    }

    var calculatedWidth = originalWidth * coversionRate;
    var calculatedHeight = originalHeight * coversionRate;

    return { calculatedWidth: calculatedWidth, calculatedHeight: calculatedHeight };
}


function updateCurrencyAndCalculate(imageIndex) {
    var selectedCurrency = document.getElementById("currencySelector_" + imageIndex).value;
    var originalPrice = parseFloat(document.getElementById("imagePrice_" + imageIndex).getAttribute("data-original-price"));
    var calculatedPrice = calculatePrice(originalPrice, selectedCurrency);
    document.getElementById("imagePrice_" + imageIndex).innerText = "Price(Picture): " + calculatedPrice.toFixed(2) + " " + selectedCurrency;
}

function calculatePrice(originalPrice, selectedCurrency) {
    var exchangeRate;

    switch (selectedCurrency) {
        case 'USD':
            exchangeRate = 1;
            break;

        case 'BAHT':
            exchangeRate = 34.86;
            break;
        case 'MMK':
            exchangeRate = 3500;
        // Add more cases as needed
    }

    var calculatedPrice = originalPrice * exchangeRate;
    return calculatedPrice;
}
