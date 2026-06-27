
async function runSearch(type){

    const trace =
        document.getElementById(
            "search-trace"
        );

    trace.innerHTML = "";

    const allNodes =
        document.querySelectorAll(
            ".graph-node"
        );

    allNodes.forEach(node => {

        node.classList.remove(
            "active-node"
        );

        node.classList.remove(
            "visited-node"
        );

        node.classList.remove(
            "goal-reached"
        );

    });

    document.getElementById(
        "expanded-count"
    ).innerText = "0";

    document.getElementById(
        "frontier-count"
    ).innerText = "0";

    document.getElementById(
        "heuristic-cost"
    ).innerText = "0";

    document.getElementById(
        "goal-status"
    ).innerText = "Searching";

    const response = await fetch(

        `/api/run-search/${type}`

    );

    const data = await response.json();

    let expanded = 0;

    const nodeSequence = [

        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G"

    ];

    data.steps.forEach((step, index) => {

        setTimeout(() => {

            trace.innerHTML += `

                <div class="trace-line success">

                    <div class="trace-title">

                        ${type.toUpperCase()} Search

                    </div>

                    <div class="trace-description">

                        ${step}

                    </div>

                </div>

            `;

            trace.scrollTop =
                trace.scrollHeight;

            const nodeId =

                `node-${nodeSequence[index]}`;

            const node =
                document.getElementById(
                    nodeId
                );

            if(node){

                node.classList.add(
                    "active-node"
                );

                setTimeout(() => {

                    node.classList.remove(
                        "active-node"
                    );

                    node.classList.add(
                        "visited-node"
                    );

                }, 600);

            }

            expanded++;

            document.getElementById(
                "expanded-count"
            ).innerText = expanded;

            document.getElementById(
                "frontier-count"
            ).innerText =

                Math.max(
                    1,
                    expanded - 1
                );

            document.getElementById(
                "heuristic-cost"
            ).innerText =

                Math.max(
                    0,
                    100 - expanded * 9
                );

            if(

                index ===
                data.steps.length - 1

            ){

                document
                    .getElementById(
                        "node-G"
                    )
                    .classList.add(
                        "goal-reached"
                    );

                document.getElementById(
                    "goal-status"
                ).innerText =

                    "Goal Reached";
            }

        }, index * 1000);

    });

}

