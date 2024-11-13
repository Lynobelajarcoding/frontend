$(document).ready(function() {
    // Data daerah kota
    const daerah = ['Banyuwangi', 'Jember', 'Probolinggo', 'Surabaya'];
    
    // Ongkir
    const ongkir = {
        'Banyuwangi': {
            'Banyuwangi': 5000,
            'Jember': 7500,
            'Probolinggo': 10000,
            'Surabaya': 15000
        },
        'Jember': {
            'Banyuwangi': 7500,
            'Jember': 5000,
            'Probolinggo': 8500,
            'Surabaya': 12500
        },
        'Probolinggo': {
            'Banyuwangi': 10000,
            'Jember': 8500,
            'Probolinggo': 5000,
            'Surabaya': 6500
        },
        'Surabaya': {
            'Banyuwangi': 15000,
            'Jember': 12500,
            'Probolinggo': 6500,
            'Surabaya': 5000
        }
    };

    // Mengisi opsi kota
    daerah.forEach(kota => {
        $('#kotaAsal').append(`<option value="${kota}">${kota}</option>`);
        $('#kotaTujuan').append(`<option value="${kota}">${kota}</option>`);
    });

    // Fungsi untuk menghitung biaya berdasarkan berat
    function menghitungBiayaBarang(beratBarang) {
        if (beratBarang <= 1) {
            return 1500;
        } else if (beratBarang <= 5) {
            return 2500;
        } else if (beratBarang <= 10) {
            return 3500;
        } else {
            return 4500;
        }
    };

    // Fungsi untuk menghitung total biaya
    function totalKeseluruhan() {
        const beratBarang = parseFloat($('#beratBarang').val()) || 0;
        const asal = $('#kotaAsal').val();
        const tujuan = $('#kotaTujuan').val();

        if (beratBarang && asal && tujuan) {
            const biayaBarang = menghitungBiayaBarang(beratBarang);
            const jarak = ongkir[asal][tujuan];
            const total = biayaBarang + jarak;

            $('#totalBiaya').val(`Rp ${total.toLocaleString('id-ID')}`);
        }
    };

    // Event listeners
    $('#beratBarang, #kotaAsal, #kotaTujuan').on('change', totalKeseluruhan);

    // Tambahan validasi untuk input berat
    $('#beratBarang').on('input', function() {
        const value = $(this).val();
        if (value < 0) {
            $(this).val(0);
        }
    });
});