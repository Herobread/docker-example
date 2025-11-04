up:
	podman compose -f backend-1/compose.yml up -d
	podman compose -f frontend/compose.yml up -d
	
	podman compose -f backend-1/compose.yml logs -f &
	podman compose -f frontend/compose.yml logs -f


down:
	podman compose -f backend-1/compose.yml down
	podman compose -f frontend/compose.yml down

