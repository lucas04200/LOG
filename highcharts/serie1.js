Highcharts.chart('serie1',
{
        chart: {
            type: 'pie'
        },
		title: {
			text: 'Analyse de auth.log'
		},
		subtitle: {
			text: 'Users inconnu utilise pour des attaques SSH'
		},
        series: [{
            data: [ 
 [ 'user' , 517], 

 [ 'admin' , 328], 

 [ 'test' , 138], 

 [ 'sage' , 85], 

 [ 'pi' , 77], 

 [ 'erp' , 76], 

 [ 'beerp' , 75], 

 [ 'be' , 73], 

 [ 'oracle' , 56], 

 [ 'ubnt' , 55], 

 [ 'ubuntu' , 50], 

 [ 'ftpuser' , 48], 

 [ 'dev' , 48], 

 [ 'postgres' , 43], 

]

 }]

 });
