// Data buah-buahan
const fruits = {
    'nanas': { price: 7500, discount: 5 },
    'anggur': { price: 35000, discount: 15 },
    'melon': { price: 12500, discount: 10 },
    'semangka': { price: 35500, discount: 10 },
    'lemon': { price: 15500, discount: 10 }
};

// Fungsi untuk mengecek dan menampilkan data buah
function checkFruit() {
    // Mengambil nilai input dan mengubah ke lowercase
    const input = document.getElementById('buahInput').value.toLowerCase();
    
    // Mengambil referensi elemen untuk menampilkan hasil
    const namaBuahEl = document.getElementById('namaBuah');
    const hargaKgEl = document.getElementById('hargaKg');
    const diskonEl = document.getElementById('diskon');

    // Mengecek apakah buah tersedia
    if (fruits[input]) {
        // Jika buah tersedia, tampilkan datanya
        namaBuahEl.textContent = input.charAt(0).toUpperCase() + input.slice(1);
        hargaKgEl.textContent = fruits[input].price.toLocaleString('id-ID');
        diskonEl.textContent = fruits[input].discount + '%';
    } else {
        // Jika buah tidak tersedia, reset tampilan dan tampilkan peringatan
        namaBuahEl.textContent = 'Buah tidak tersedia';
        hargaKgEl.textContent = '.................';
        diskonEl.textContent = '.................';
        alert('Buah tidak tersedia dalam daftar!');
    }
}

// Event listener untuk input ketika user menekan Enter
document.getElementById('buahInput').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        checkFruit();
    }
});