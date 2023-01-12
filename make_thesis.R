# render thesis
library("quarto")

# html

#quarto_render(output_format = "html")

# word document

#quarto_render(output_format = "docx")


#pdf
#install.packages("tinytex")
#tinytex::install_tinytex() install tinytex for processing LaTeX files

quarto_render(output_format = "pdf")


#both pdf and html
#quarto_render()
