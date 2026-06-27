async function runFullPipeline(){

    const trace = document.getElementById(
        "reasoning-trace"
    );

    trace.innerHTML = "";

    const response = await fetch(
        "/api/full-ai-pipeline"
    );

    const data = await response.json();

    data.pipeline.forEach((step, index) => {

        setTimeout(() => {

            trace.innerHTML += `

                <div class="trace-line success">

                    <div class="trace-title">
                        AI Pipeline Step
                    </div>

                    <div class="trace-description">
                        ${step}
                    </div>

                </div>

            `;

            trace.scrollTop =
                trace.scrollHeight;

        }, index * 700);

    });

}