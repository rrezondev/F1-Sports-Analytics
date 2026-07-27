const ctx = document.getElementById('driversChart');

new Chart(ctx, {

    type: 'bar',

    data: {

        labels: [
            'VER',
            'HAM',
            'NOR',
            'LEC',
            'RUS'
        ],

        datasets: [{

            label: 'Points',

            data: [
                1200,
                1100,
                900,
                850,
                700
            ]

        }]

    },

    options: {

        responsive: true

    }

});