from django.shortcuts import render
from .models import Category,Ürün

katagori_liste =["erkek","kadın","Çocuk","ev yaşam","tekneloji"]
urunler_list = [
    {
        "id":1,
        "ürün_adı": "Bebek Giyim",
        "aciklama": "Bebek giyim açıklama özelliği",
        "resim":"1.jpg",
        "anasayfa": True
    },
    {
        "id":2,
        "ürün_adı": "Kadın Giyim",
        "aciklama": "Kadın Giyim açıklaması özelliği",
        "resim":"6.jpg",
        "anasayfa": True
    },
    {
        "id":3,
        "ürün_adı": "Erkek Giyim",
        "aciklama": "Erkek Giyim açıklaması özelliği",
        "resim":"7.jpg",
        "anasayfa": False
    },
    {
        "id":4,
        "ürün_adı": "Elektirikli Ev Aletleri",
        "aciklama": "Elektirikli Ev Aletleri açıklaması özelliği",
        "resim":"8.jpg",
        "anasayfa": True
    },
    {
        "id":5,
        "ürün_adı": "Teknoloji",
        "aciklama": "Tekneloji bilgisayar açıklaması özelliği",
        "resim":"5.jpg",
        "anasayfa": False
    }
]

def home(reqest):
    data={
        "katagoriler": Category.objects.all(),
        "ürünler": Ürün.objects.filter(anasayfa=True)
    }
    return render(reqest, "index.html", data)

def erkek(reqest):
    data={
        "katagoriler": Category.objects.all(),
        "ürünler": Ürün.objects.all()
    }
    return render(reqest, "erkek.html",data)

def kadın(reqest):
    data={
        "katagoriler": Category.objects.all(),
        "ürünler": Ürün.objects.all()
    }
    return render(reqest, "kadın.html",data)

def cocuk(reqest):
    data={
        "katagoriler": Category.objects.all(),
        "ürünler": Ürün.objects.all()
    }
    return render(reqest, "cocuk.html",data)

def evyasam(reqest):
    data={
        "katagoriler": Category.objects.all(),
        "ürünler": Ürün.objects.all()
    }
    return render(reqest, "evyasam.html",data)

def tekneloji(reqest):
    data={
        "katagoriler": Category.objects.all(),
        "ürünler": Ürün.objects.all()
    }
    return render(reqest, "teknoloji.html",data)

def _details(reqest, id):
    data={
        "ürün": Ürün.objects.get(id=id)
    }
    return render(reqest, "details.html",data)

