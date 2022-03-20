import sys, os, re

def run(path='doc/pylint'):
    files = []
    for filename in os.listdir(path):
        if filename == 'pylint_global.html':
            pass # ignore for now
        elif filename.startswith('pylint_') and filename.endswith('.html'):
            with open(os.path.join(path, filename), "r+") as f:
                contents = f.read().strip()
                if len(contents) > 0:
                    files.append(filename[7:-5])
                    f.seek(0)
                    f.write(contents.replace('<body>', '<body><p><a href="pylint_global.html">Index</a></p>'))
        # else ignore

    files.sort(key=len, reverse=True)

    with open(os.path.join(path, 'pylint_global.html'), "r+") as f:
        contents = f.read()
        for filename in files:
            contents = re.sub('([^A-Za-z_>])%s' % filename, r'\1<a href="pylint_%s.html">%s</a>' % (filename, filename), contents)
            contents = re.sub('^%s' % filename, '<a href="pylint_%s.html">%s</a>' % (filename, filename), contents)
        contents = contents.replace('errors / warnings by module', '<a name="errors_warnings"></a>errors / warnings by module')
        f.seek(0)
        f.write(contents)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        run()
