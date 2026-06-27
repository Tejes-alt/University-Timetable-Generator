async function runCSP(){

    const trace =
        document.getElementById(
            "csp-trace"
        );

    trace.innerHTML = `

        <div class="trace-line info">

            <div class="trace-title">

                Initializing CSP Engine

            </div>

            <div class="trace-description">

                Loading constraint propagation...

            </div>

        </div>

    `;

    try{

        const response = await fetch(
            "/api/run-csp"
        );

        if(!response.ok){

            throw new Error(
                "CSP execution failed"
            );

        }

        const data = await response.json();

        trace.innerHTML = "";

        data.steps.forEach((step, index) => {

            setTimeout(() => {

                trace.innerHTML += `

                    <div class="trace-line success">

                        <div class="trace-title">

                            CSP Execution

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

        setTimeout(() => {

            trace.innerHTML += `

                <div class="trace-line info">

                    <div class="trace-title">

                        Explainability Engine

                    </div>

                    <div class="trace-description">

                        ${data.explanations.join("<br><br>")}

                    </div>

                </div>

            `;

            trace.innerHTML += `

                <div class="trace-line success">

                    <div class="trace-title">

                        Final Assignment

                    </div>

                    <div class="trace-description">

                        ${JSON.stringify(
                            data.assignment,
                            null,
                            2
                        )}

                    </div>

                </div>

            `;

        }, data.steps.length * 750);

    }

    catch(error){

        trace.innerHTML = `

            <div class="trace-line fail">

                <div class="trace-title">

                    CSP Engine Failure

                </div>

                <div class="trace-description">

                    ${error.message}

                </div>

            </div>

        `;

    }

}