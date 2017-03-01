import fresh_tomato
import media
raees=media.Movie("RAEES","A GUJRAT SMUGLER","/home/fiha/ud1/pics/srk.jpg","https://www.youtube.com/watch?v=J7_1MU3gDk0")
sultan=media.Movie("SULTAN","WRESTLER'S LOVESTORY","/home/fiha/ud1/pics/salman.jpg","https://www.youtube.com/watch?v=wPxqcq6Byq0")
dangal=media.Movie("DANGAL",
"HOW GIRLS CAN TAKE PART IN ALL WORK",
"/home/fiha/ud1/pics/aamir.jpeg",
"https://www.youtube.com/watch?v=x_7YlGv9u1g")
haider=media.Movie("HAIDER","LIFE OF A KASHMIRI MILITANTS","/home/fiha/ud1/pics/shahid.jpeg","https://www.youtube.com/watch?v=ZmN_VSo8DOo")
ashiki2=media.Movie("AASHIQUI2","LIFE OF TWO SINGER ","/home/fiha/ud1/pics/shraddha.jpeg","https://www.youtube.com/watch?v=FyXXgpPqe6w")
badlapur=media.Movie("BADLAPUR","REVENGE AFTER 15 YEAR","/home/fiha/ud1/pics/vd.jpeg","https://www.youtube.com/watch?v=9KEoZanqlOE")
movies=[raees,sultan,dangal,haider,ashiki2,badlapur]
fresh_tomato.open_movies_page(movies)
