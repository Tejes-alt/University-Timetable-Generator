async function runMinimax(){

    const trace =
        document.getElementById(
            "decision-trace"
        );

    trace.innerHTML = "";

    const response = await fetch(
        "/api/run-minimax"
    );

    const data = await response.json();

    data.steps.forEach((step, index) => {

        setTimeout(() => {

            trace.innerHTML += `

                <div class="trace-line success">

                    <div class="trace-title">
                        Decision Agent
                    </div>

                    <div class="trace-description">
                        ${step}
                    </div>

                </div>

            `;

        }, index * 700);

    });

}