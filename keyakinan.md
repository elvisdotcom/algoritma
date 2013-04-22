
# Menghitung nilai keyakinan berdasarkan penilaian positif dan negatif dari pemilih


Algoritma ini memperlakukan input sebagai statistik contoh. Algoritma ini juga memberikan penilaian sementara (provisional ranking) sebesar 85%. Semakin banyak input, semakin besar nilai keyakinan dengan nilai yang sebenarnya. 

Penilaian [interval Wilson](http://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval) dipilih karena cocok untuk uji coba berskala kecil dan/atau memiliki kemungkinan yang sangat ekstrim. Notasi matematikanya

![](https://raw.github.com/ardwort/algoritma-pembelajaran-mesin/master/images/interval_Wilson.png)

dengan parameter yang didefinisikan:

* ![](https://raw.github.com/ardwort/algoritma-pembelajaran-mesin/master/images/p.png) adalah fraksi yang diamati dari penilaian positif
* ![](https://raw.github.com/ardwort/algoritma-pembelajaran-mesin/master/images/n.png) adalah jumlah total penilaian
* ![](https://raw.github.com/ardwort/algoritma-pembelajaran-mesin/master/images/z_1-frac_alpha_2.png) adalah peringkat percentil ![](https://raw.github.com/ardwort/algoritma-pembelajaran-mesin/master/images/1-frac_1_2-alpha.png) dari standar distribusi normal

