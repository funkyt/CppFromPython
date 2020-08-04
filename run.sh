# Script to update generated HTML from templates + md files,
# then start a simple local webbrowser so we can preview the slides.

mkdir -p html
for F in lectures/*.md ; do
    cat slide.head.html $F slide.foot.html > html/$(basename ${F%.md}).html
    
done

cd html ; python3 -m http.server 8000