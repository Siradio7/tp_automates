%{
#include <stdio.h>
%}

%%
[0-9]+"\\."[0-9]+    { printf("Nombre flottant : %s\n", yytext); }
[ \t\n]+             ;   /* ignorer espaces et retours à la ligne */
.                    { /* ignorer tout le reste */ }
%%

int main(int argc, char *argv[]) {
    yylex();
    return 0;
}
