import re

with open('/home/gonenc/projects/mat205/private/mat205/source/tex/notes/cours.tex', 'r') as f:
    content = f.read()

replacement = r"""Par exemple, dans $\Z[\sqrt{-5}]$, l'élément $6$ a deux factorisations : $2 \cdot 3$ et $(1+\sqrt{-5})(1-\sqrt{-5})$. Au niveau des idéaux, on a $(6) = (2)(3)$ et $(6) = (1+\sqrt{-5})(1-\sqrt{-5})$. Or, les idéaux $(2)$ et $(3)$ ne sont pas premiers ! Ils se décomposent en idéaux premiers : $(2) = \mathfrak{p}_2^2$, $(3) = \mathfrak{p}_3 \mathfrak{q}_3$, $(1+\sqrt{-5}) = \mathfrak{p}_2 \mathfrak{p}_3$, et $(1-\sqrt{-5}) = \mathfrak{p}_2 \mathfrak{q}_3$. Ainsi, les deux factorisations en éléments correspondent \emph{exactement} à deux manières de regrouper l'unique factorisation en idéaux premiers : $(6) = \mathfrak{p}_2^2 \mathfrak{p}_3 \mathfrak{q}_3 = (\mathfrak{p}_2^2)(\mathfrak{p}_3\mathfrak{q}_3) = (\mathfrak{p}_2\mathfrak{p}_3)(\mathfrak{p}_2\mathfrak{q}_3)$."""

# We will replace the text starting from "La factorisation unique est ainsi \og sauvée\fg{} au niveau des idéaux. Par exemple, dans..." to "...où chaque facteur est un idéal premier."

pattern = re.compile(r"La factorisation unique est ainsi\\n\\og sauvée\\fg\{\} au niveau des idéaux\. Par exemple, dans\\n.*?où chaque facteur est un idéal premier\.", re.DOTALL)

new_content = pattern.sub(replacement, content)

with open('/home/gonenc/projects/mat205/private/mat205/source/tex/notes/cours.tex', 'w') as f:
    f.write(new_content)
