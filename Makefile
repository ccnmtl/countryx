APP=countryx
JS_FILES=media/js/game.js media/js/faculty.js media/js/sim_allpaths.js
MAX_COMPLEXITY=7

all: eslint jenkins

include *.mk
