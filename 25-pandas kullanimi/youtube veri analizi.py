import pandas as pd

print("Tum veriler:\n") 
df = pd.read_csv("DEvideos.csv")
print(df)

print("*************************1.cevap***********************************************")
# 1- İlk 10 kaydı getiriniz.
print("ilk 10 kayit:\n")
sonuc = df.head(10)
print(sonuc)

print("*************************2.cevap***********************************************")
# 2- İkinci 5 kaydı getiriniz.
print("ikinci 5 kaydi:\n")
sonuc1 = df[5:10]
print(sonuc1)

print("************************3.cevap************************************************")
# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
print("Datadette bulunan kolon isimleri:\n")
sonuc2 = df.columns
print(sonuc2)
sonuc2a = len(df.columns)
print(f"Kolon sayisi: {sonuc2a}")

print("************************4.cevap************************************************")
# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description,trending_date)
try:
    sonuc3 = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"], axis=1)
    print("Guncel dataframe:\n")
    print(sonuc3)
except KeyError as e:
    print(f"Hata: {e}")

print("***********************5.cevap*************************************************")
# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
like_mean = df["likes"].mean()
print(f"Like ortalamasi: {like_mean}")

dislike_mean = df["dislikes"].mean()
print(f"Dislike ortalamasi: {dislike_mean}")

print("**********************6.cevap**************************************************")
# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
sonuc5 = df.head(50)[["title","likes","dislikes"]]
print("ilk 50 videonun like ve dislike kolonlari:\n")
print(sonuc5)

print("*********************7.cevap***************************************************")
# 7- En çok görüntülenen video hangisidir ?
most_viewed_title = df[df["views"] == df["views"].max()]["title"].iloc[0]
print(f"En cok goruntulenen video: {most_viewed_title}")

print("********************8.cevap****************************************************")
# 8- En düşük görüntülenen video hangisidir?
least_viewed_title = df[df["views"] == df["views"].min()]["title"].iloc[0]
print(f"En dusuk goruntulenen video: {least_viewed_title}")

print("*******************9.cevap*****************************************************")
# 9- En fazla görüntülenen ilk 10 video hangisidir ?
top_10_videos = df.sort_values("views", ascending=False).head(10)[["title","views"]]
print("En fazla goruntulenen ilk 10 video:\n")
print(top_10_videos)

print("*******************10.cevap****************************************************")
# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
likes_by_category = df.groupby("category_id")["likes"].mean().sort_values(ascending=False)
print("Kategoriye gore begeni ortalamalari:\n")
print(likes_by_category)

print("*******************11.cevap****************************************************")
# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
comments_by_category = df.groupby("category_id")["comment_count"].sum().sort_values(ascending=False)
print("Kategoriye gore yorum sayilari:\n")
print(comments_by_category)

print("*******************12.cevap****************************************************")
# 12- Her kategoride kaç video vardır?
videos_per_category = df["category_id"].value_counts()
print("Her kategorideki video sayisi:\n")
print(videos_per_category)

print("******************13.cevap*****************************************************")
# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df["title_len"] = df["title"].apply(len)
print("Title uzunluklari:\n")
print(df[["title", "title_len"]])

print("*****************14.cevap*****************************************************")
# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
df["tags_count"] = df["tags"].apply(lambda x: len(x.split('|')))
print("Tag sayilari:\n")
print(df[["tags", "tags_count"]])

print("****************15.cevap******************************************************")
# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)
df["like_dislike_ratio"] = df["likes"] / (df["dislikes"] + 1)  # +1 paydanin 0 olmasini onlemek icin
popular_videos = df.sort_values("like_dislike_ratio", ascending=False)[["title", "like_dislike_ratio"]]
print("En populer videolar:\n")
print(popular_videos)

print("**********************15.cevap(2)**********************************************")

def likeDislikeGoreHesapla(dataset):
    likeList=list(dataset["likes"])
    dislikeList=list(dataset["dislikes"])

    liste=list(zip(likeList,dislikeList))

    oranListesi=[]

    for like,dislike in liste:
        if(like + dislike)==0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))
        
    return oranListesi

df["begeniOrani"]=likeDislikeGoreHesapla(df)
print(df.sort_values("begeniOrani",ascending=False)[["title","likes","dislikes","begeniOrani"]])

# parantezlere dikkat!!!

