Convert a pdf to images using `pdftoppm`, provided by **Poppler** or **xpdf**.


##kbmt-tv-ad.pdf

This is an image-based pdf from <https://stations.fcc.gov/collect/files/10150/Political%20File/2014/State/Abbott%20Greg%20Texas%20Attorney%20General/9358799ABBOTTGREGKBMT%20(14043372643700)_.pdf> (Since removed by station, KBMT).

## Everytown-for-Gun-Safety-AF-909199-14062383009820.pdf

Text-based pdf from <https://stations.fcc.gov/collect/files/35486/Political%20File/2014/Non-Candidate%20Issue%20Ads/Everytown%20for%20Gun%20Safety%20Action%20Fund/Everytown%20for%20Gun%20Safety%20909199%20(14065814829588).pdf>.

## Converting to image files

```
pdftoppm -r 300 Everytown-for-Gun-Safety-AF-909199-14062383009820.pdf Everytown-for-Gun-Safety-AF

pdftoppm -r 300 kbmt-tv-ad.pdf kbmt-tv-ad

```