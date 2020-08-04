echo "Hello"

mkdir html
for F in lecture.* ; do
    echo $F ${F%.md}
done

cd html ; python3 -m http.server 8000