async function runBayesian(){

    const trace =
        document.getElementById(
            "bayes-trace"
        );

    trace.innerHTML = "";

    const response = await fetch(
        "/api/run-bayes"
    );

    const data = await response.json();

    data.inference_steps.forEach(
        (step, index) => {

        setTimeout(() => {

            trace.innerHTML += `

                <div class="trace-line info">

                    <div class="trace-title">
                        Bayesian Inference
                    </div>

                    <div class="trace-description">
                        ${step}
                    </div>

                </div>

            `;

        }, index * 700);

    });

}