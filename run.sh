echo "Hello"

mkdir -p html
for F in lectures/*.md ; do
    cat slide.head.html $F slide.foot.html > html/$(basename ${F%.md}).html
done

cd html ; python3 -m http.server 8000