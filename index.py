from glob import glob
import time

exclude = open(".indexignore").readlines()

def main():
    start = time.process_time()
    print("indexer started.")
    files = glob("**/*.md", recursive=True)
    print("indexed files.")

    print("now writing files.")
    with open("page_index.md", "w") as file:
        file.truncate(0) # reset it
        file.write("---\ntitle: Page Index\n---\n\n")
        file.write("# Page Index\n\n")
        file.write("*if there is an issue, please submit a [bug report](https://github.com/Just-a-Unity-Dev/sector/issues/new/choose)*\n\n")
        
        category = None
        subcategory = None

        file.write("## Meta\n\n")
        for markdown in files:
            if markdown.startswith("build") or markdown in exclude:
                continue
                
            categories = markdown.replace("\\", "/").split("/")
            name = categories.pop()[:-3].replace("_", " ").title()
            
            # this could be so much more efficient, oh well
            if len(categories) > 0:
                if category != categories[0]:
                    file.write(f"\n## {categories[0].capitalize()}\n\n")
                    category = categories[0]
            
            if len(categories) > 1:
                if subcategory != categories[1]:
                    file.write(f"\n### {categories[1].capitalize()}\n\n")
                    subcategory = categories[1]

            if len(categories) > 2:
                name += f" ({categories[2]})"
            
            if name == "Index":
                name = "Homepage"

            file.write(f"- [{name}]({markdown[:len(markdown) - 3]})\n")
            
    end = time.process_time()

    print(f"finished in {(end - start) * 10**3}ms.")

if __name__ == "__main__":
    main()
