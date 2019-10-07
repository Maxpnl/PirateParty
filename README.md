# Pirate Party Assignment
## Brief description
This is the project I built for the assignment requested by the Pirate Party, I decided to make this opensource as this could help other people get inspired, this is a really basic project, it has just 3 pages, the homepage (the first one) is a list of PDF files, if you click on one of them you will be able to see it's content from the browser (this is the second page) and download it, the last one is a more "design-based" page which explains why schools should switch to Linux as their main operating system.
## Tools/Libraries/Images/Fonts used
1. **pdf.js** ([github](https://mozilla.github.io/pdf.js/)) *used in the PDF view page*
2. **animate.css** ([github](https://github.com/daneden/animate.css)) *used in the "Why should schools switch to Linux" page*
3. **bootstrap** ([github](https://github.com/twbs/bootstrap)) *used in every page*
4. **flaticon** ([main site](https://www.flaticon.com/)) *svgs for the Linux page*
## Features
You can add as many PDFs as you want, even though there isn't an upload form but you can move the PDF file you want to upload inside the media folder and add a new **PdfFile** inside the django administration page (located at */admin*), with it's file name and display name, while the slug is generated from the file name every time you save it.