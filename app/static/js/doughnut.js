let covidChart = document.getElementById('covidData').getContext('2d');

Chart.defaults.global.defaultFontFamily = 'Lato';
Chart.defaults.global.defaultFontSize = 12;
Chart.defaults.global.defaultFontColor = '#777';

let doughnutChart = new Chart(covidChart, {
    type: 'doughnut',
    data: {
        labels: ['ဓာတ်ခွဲစစ်ဆေးသူစုစုပေါင်း', 'စောင့်ကြည့်လူနာစုစုပေါင်း', 'ပိုးတွေ့', 'ပိုးတွေ့ပြန်လည်သက်သာ', 'သေဆုံးလူနာ'],
        datasets: [{
            label: 'မြန်မာ covid-19 ဖြစ်စဉ်များ',
            data: [
                49729,
                5486,
                261,
                167,
                6
            ],
            backgroundColor: [
                '#1c7bff',
                '#ff861d',
                '#fff823',
                '#92ff4e',
                '#ff3810',
            ],
            borderWidth: 1,
            borderColor: '#777',
        }]
    },
    options: {
        title: {
            display: true,
            text: 'Covid-19',
            fontSize: 12,
            reponsive: true, 
            
        },
        legend: {
            display: true,
            position: 'right',
            labels: {
                fontColor: '#000'
            }
        },
        layout: {
            padding: {
                left: 50,
                right: 0,
                bottom: 0,
                top: 10
            }
        },
        tooltips: {
            enabled: true
        }
    }
}); 