# Api de whisper para convertir audio a texto

## Instalación

- requiere python 3
- requiere pip
- requiere venv
- requiere ffmpeg
- sistema operativo linux

_nota_: se recomienda crear un entorno virtual para la instalación de las dependencias

_nota_: se recomienda instalar ffmpeg desde los repositorios de su distribución linux

_nota_: $ indica que se debe ejecutar en la terminal

## Instalación de dependencias

```bash
$ sudo apt-get install pip venv ffmpeg
```

## Creación de entorno virtual

```bash
$ python3 -m venv venv
```

## Activación de entorno virtual

```bash
$ source env/bin/activate
```

## Instalación de dependencias

```bash
$ pip install requirements.txt
```

## Ejecución

```bash
$ flask run
```

# endpoints de la api

## /text

**POST** - recibe un archivo de audio y devuelve el texto del audio

nota: el archivo de audio se manda por el body de la petición en formato multipart/form-data

## /transcribe

**POST** - recibe un archivo de audio y devuelve el texto del audio en inglés

nota: el archivo de audio se manda por el body de la petición en formato multipart/form-data

## /translate/<lang>

**POST** - recibe un archivo de audio y devuelve el texto del audio en el idioma especificado

lista de idiomas disponibles:

af,am,ar,as,az,ba,be,bg,bn,bo,br,bs,ca,cs,cy,da,de,el,en,es,et,eu,fa,fi,fo,fr,gl,gu,ha,haw,he,hi,hr,ht,hu,hy,id,is,it,ja,jw,ka,kk,km,kn,ko,la,lb,ln,lo,lt,lv,mg,mi,mk,ml,mn,mr,ms,mt,my,ne,nl,nn,no,oc,pa,pl,ps,pt,ro,ru,sa,sd,si,sk,sl,sn,so,sq,sr,su,sv,sw,ta,te,tg,th,tk,tl,tr,tt,uk,ur,uz,vi,yi,yo,zh
