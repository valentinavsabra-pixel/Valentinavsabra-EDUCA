for file in app/page.tsx components/Footer.tsx app/login/page.tsx; do
  perl -0777 -i -pe 's/\\n/\n/g' "$file"
done
