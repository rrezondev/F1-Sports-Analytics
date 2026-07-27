// DRIVER POINTS

new Chart(document.getElementById('pointsChart'), {

    type: 'bar',

    data: {

        labels: [
            'PIA',
            'NOR',
            'VER',
            'RUS',
            'LEC'
        ],

        datasets: [{

            label: 'Points',

            data: [
                541,
                448,
                418,
                343,
                287
            ],

            borderWidth: 2,
            borderRadius: 12

        }]

    },

    options: {

        responsive: true,
        maintainAspectRatio: false

    }

});


// TIRE STRATEGY

new Chart(document.getElementById('tireChart'), {

    type: 'doughnut',

    data: {

        labels: [
            'SOFT',
            'MEDIUM',
            'HARD'
        ],

        datasets: [{

            data: [
                35,
                45,
                20
            ],

            borderWidth: 2

        }]

    },

    options: {

        responsive: true,
        maintainAspectRatio: false

    }

});


// PIT STOPS

new Chart(document.getElementById('pitChart'), {

    type: 'line',

    data: {

        labels: [
            'VER',
            'NOR',
            'LEC',
            'HAM',
            'RUS'
        ],

        datasets: [{

            label: 'Pit Stops',

            data: [
                2.1,
                2.3,
                2.5,
                2.8,
                2.2
            ],

            borderWidth: 3,
            tension: 0.4

        }]

    },

    options: {

        responsive: true,
        maintainAspectRatio: false

    }

});