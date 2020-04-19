# supermarket

Portugal supermarket items price.  

## Introduction

Online shopping have been providing us:  
* convenient way to shopping;  
* transparency on product prices;  
* visibility;  

As all we know the current situation, it is also providing us:  
* safety;  
* fulfill the quarantine;  

Nevertheless, every supermarket has its own price on the same product.  

## Goals

This is a open-source project aims to collect dataset about Portugal supermarket.  
Clarifying the purpose, this is only for learning and studying purposes.  
Any improvements or merge requests are welcomed.

## Development

Right now, there are samples scripts to collect data (cat food).  
There are following options for <samples> below:  
* auchansample
* continentesample
* elcorteinglessample

__Note:__  
This is developed using PyCharm. To run on PyCharm idea see [link](https://stackoverflow.com/a/22254926).  
Last update on 19/04/2020.


### Enrivonemt

Enter the virtual environment.

### Execute
```
(venv) cd supermarket
(venv) scrapy crawl <sample>
```
### Save to a csv file
```
(venv) cd supermarket
(venv) scrapy crawl <sample> -o results/<sample>.csv
```
## Supermarkets

The following subsections show list of Portugal online shopping.  
Note: There are more. Below are supermarkets that just came to my head at writing moment. 

### The list below are supermarkets that provide online shopping (the project's focuses)  

- [x] [Auchan](https://www.auchan.pt/)
- [x] [Continente](https://www.continente.pt/stores/continente/pt-pt/public/Pages/homepage.aspx)
- [x] [ElCorteInglés](https://www.elcorteingles.pt/supermercado/)

### The list below are supermarkets that provide online shopping but you have to bring up yourself  

- [ ] [Intermarche](https://lojaonline.intermarche.pt/)

### The list below are supermarkets that DOES NOT provide online shopping (we won't focus on these)  

- [Aldi](https://www.aldi.pt/)
- [Lidl](https://www.lidl.pt/)
- [Minipreço](https://www.minipreco.pt/)
- [Pingo Doce](https://www.pingodoce.pt/)

