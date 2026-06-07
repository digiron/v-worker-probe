# v-worker-probe

Synthetic throwaway target for the v-agency spec-07 execution capability.

This repo exists **only** to prove the agency's `spawn_worker` build loop end-to-end:
clone -> author -> validate -> branch -> PR. No real roadmap work lands here.
Workers push branches named `worker/spec-07/<delegation_id>` and open PRs for Ron
to review and merge; the agency's GitHub-App token carries no merge scope.
