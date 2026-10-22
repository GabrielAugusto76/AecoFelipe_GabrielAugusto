#!/usr/bin/env bash
set -e

case "$1" in
  1)
    [ -d .git ] || git init -b main
    git add .gitignore requirements.txt docs/matriz_decisao.md \
            career_expert/__init__.py career_expert/compat.py career_expert/questions.py
    git commit -m "feat: estrutura inicial, matriz de decisão e catálogo de trilhas/perguntas (Fase 1)"
    ;;
  2)
    git add career_expert/__init__.py career_expert/compat.py career_expert/questions.py career_expert/engine.py app.py
    git commit -m "feat: base de conhecimento Experta (25 regras) e interface Streamlit (Fases 2 e 3)"
    ;;
  3)
    git add career_expert/personas.py tests/test_personas.py README.md fazer_commits.sh
    git commit -m "test/docs: 10 personas de validação, testes e README (Fases 4 e 5)"
    ;;
  *)
    echo "Uso: bash fazer_commits.sh [1|2|3]"
    exit 1
    ;;
esac

echo
git log --oneline
echo
echo "Enviar ao GitHub:"
echo "  (1ª vez) git remote add origin https://github.com/SEU-USUARIO/consultor-carreiras-ti.git"
echo "  git push -u origin main"
