SHELL      	:= /bin/bash

NAME		:= notebook
VOL		:= 1
ORG_DIR  	:= VOL$(VOL)
IMG_DIR		:= $(ORG_DIR)/img
PAGES	    	:= 10
SCRIPT      	:= $(NAME).py
BACKGROUND  	:= $(NAME).eps
NOTEBOOK    	:= $(NAME).pdf
TEX 		:= $(NAME).tex
PY_CMD 	    	:= python $(SCRIPT) $(ORG_DIR) $(IMG_DIR) $(VOL) $(PAGES)
TEX_CMD 	:= for i in {1..2}; do xelatex $(TEX); done
CMD 		:= $(PY_CMD) && $(TEX_CMD)

P_NAME		:= printable
PRT_SCRIPT	:= $(P_NAME).py
PRT_TEX		:= $(P_NAME).tex
PROOF		:= $(P_NAME).pdf
PRT_PY		:= python $(PRT_SCRIPT) $(NOTEBOOK)
PRT_CMD 	:= for i in {1..2}; do xelatex $(PRT_TEX); done
P_CMD		:= $(PRT_PY) && $(PRT_CMD)

PS		:= pdftops $(PROOF)
BOOK		:= psbook $(P_NAME).ps proofA4.ps
SIGNATURES	:= psnup -2 -Pa5 proofA4.ps finalA5.ps
C_PS		:= pstopdf finalA5.ps
FINISH_CMD	:= $(PS) && $(BOOK) && $(SIGNATURES) && $(C_PS)

ACC         	:= $(NAME).log $(NAME).aux $(NAME).tex *.png $(NOTEBOOK)
P_ACC		:= $(P_NAME).log $(P_NAME).aux $(P_NAME).tex
F_ACC		:= *.ps

.PHONY: all clean distclean

all: $(NOTEBOOK) $(PROOF) clean

$(NOTEBOOK): $(SCRIPT)
	@echo Building notebook...
	mkdir -p $(ORG_DIR) $(IMG_DIR)
	$(CMD)
	$(P_CMD)

clean:
	@- $(RM) $(ACC) $(P_ACC) $(F_ACC)

distclean: clean
