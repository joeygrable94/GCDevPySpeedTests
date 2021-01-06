# ---------------------------------------------------------------------------
# IMPORTS
from lib.SpeedTests import RunPageSpeedTests

# ---------------------------------------------------------------------------
# Set up your websites to test
websites = [
	"mountainhouseliving.com",
	"whitneyranchca.com",
	"millvillebythesea.com",
	"riverislands.com",
	"greatersmc.com",
	"chameleonoc.com",
	"getcommunity.com",
	"iheartoldtowneorange.com",
]

# run the tests on these websites
RunPageSpeedTests( websites )
