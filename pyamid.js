function printUpsideDownPyramid(height) {
	for (let i = height; i >= 1; i--) {
		// Print leading spaces
		let spaces = " ".repeat(height - i)
		// Print stars
		let stars = "*".repeat(2 * i - 1)
		console.log(spaces + stars)
	}
}

// Example usage:
const height = 5 // You can change this value to increase or decrease the height of the pyramid
printUpsideDownPyramid(height)

function printPyramid(height) {
	for (let i = 1; i <= height; i++) {
		// Print leading spaces
		let spaces = " ".repeat(height - i)
		// Print stars
		let stars = "*".repeat(2 * i - 1)
		console.log(spaces + stars)
	}
}

// Example usage:
const height = 5 // You can change this value to increase or decrease the height of the pyramid
printPyramid(height)
