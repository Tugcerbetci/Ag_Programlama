# Ag_Programlama
Ağ programlama dersi projesidir. Ağ paketleri analizi ve görselleştirilmesi. 

Ag Paketleri Analizi ve Gorsellestirilmesi Projenin amacı kullanıcılara wiresharktaki ağ paketlerini okumaları ve anlamaları konusunda kolaylık sağlamaktır. Ağ trafiği veri dosyalarını okuyarak, iletilen paketler arasındaki ilişkileri analiz etmek ve bu ilişkileri graf yapısıyla görselleştirerek kullanıcıya sunmaktır. Kullanıcı oluşturulan görselde paketleri kolaylıkla inceleyip analiz yapabilecektir. İletilen paketlerin özelliklerini, örneğin protokol türlerini, kaynak ve hedef IP adreslerini, iletilen veri miktarını vb. gibi bilgileri görsel olarak gözlemleyebilecektir. Toplanan verileri kullanarak, ağdaki bağlantıları görselleştirilecek ve farklı protokol türlerine göre paketler renklendirilecektir. Hangi ip adresinden hangi ip adresine kaç adet paket gönderildiği de paket sayısına göre görselleştirilip kalınlık sağlanacaktır. Görselleştirmeler aracılığıyla, ağ trafiğinin genel yapısını anlamak ve potansiyel anormallikleri tespit etmek temel amaçtır.

#Kullanılan_Yöntemler

Ağ trafiği veri dosyalarının JSON formatında okunması ve içeriğinin pandas DataFrame'e dönüştürülmesi. Ağ trafiği veri dosyaları JSON formatında okunur ve içeriği karmaşıklığı azaltmak için veri sözlüğüne dönüştürülür. Veriler veri sözlüğünden okunarak işlenir. İlişkilerin görselleştirilmesi için, PYVIS kütüphanesinin kullanılması ve paket bağlantılarının ağ grafiği olarak temsil edilmesi. İlişkiler, kenarlar ve düğümler için PYVIS kütüphanesi kullanılır. Paketlerin bağlantıları, renkleri, sayıları ve hareketliliği PYVIS ile sağlanır. Görselleştirmelerde farklı protokol türlerine göre renklendirme yapılır ve paket sayısına göre kalınlıklar ayarlanır. Paket sayısı fazla olan kenar daha kalın görselleştirilir. Ayrıca her protokol türü farklı renkler ile temsil edilir ve graf modelinde farklı renklerde görselleştirilir.

#Graphical_Abstact

![GRAPHİCAL ABSTRACT](https://github.com/Tugcerbetci/Ag_Programlama/assets/95607055/1f25291e-45f9-43f9-8cc8-8fa732f7491b)

#Interface_1

![1](https://github.com/Tugcerbetci/Ag_Programlama/assets/95607055/cd8e13b6-98fa-4727-9f74-bb9c3deebe04)

#Interface_2

![2](https://github.com/Tugcerbetci/Ag_Programlama/assets/95607055/f414acfa-ab57-4639-b55b-4135453bc317)



