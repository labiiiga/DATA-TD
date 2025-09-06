import sys
from collections import Counter

class Sanitizertest:
    def __init__(self, text):
        self.text = text

    def sanitize(self):
        self.text = self.text.lower()
        self.text = self.text.replace("\t", "____") 
        self.text = self.text.replace("    ", "____") #ผมแทน 4 space ด้วยเพราะว่าลองไฟล์.txt แล้วบางทีtab โดนมองเป็น4spaceแทน
        return self.text

    def stats(self):
        counts = Counter()
        for c in self.text:
            if c.isalpha():
                counts[c] += 1
        return counts

def main():
    if len(sys.argv) < 2:
        print("ต้องใส่ชื่อไฟล์")
        sys.exit(1)

    source = sys.argv[1]
    target = sys.argv[2] if len(sys.argv) > 2 else None

    f = open(source, "r", encoding="utf-8")
    raw = f.read()
    f.close()

    sanitizer = Sanitizertest(raw)
    clean = sanitizer.sanitize()
    stats = sanitizer.stats()

    result = "ผลลัพธ์หลังsanitizer\n" + clean + "\n\nสถิติตัวอักษร\n"
    for k in sorted(stats.keys()):
        result += f"{k}: {stats[k]}\n"
    print(result)

    if target:
        out = open(target, "w", encoding="utf-8")
        out.write(result)
        out.close()

if __name__ == "__main__":
    main()
