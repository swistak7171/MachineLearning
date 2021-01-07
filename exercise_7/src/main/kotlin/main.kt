import krangl.*

private const val X1_HEADER: String = "X1"
private const val X2_HEADER: String = "X2"
private const val A_HEADER: String = "a"

private val SINGLE_DATA = listOf(
    0,
    1
)

private val DOUBLE_DATA = listOf(
    0 to 0,
    0 to 1,
    1 to 0,
    1 to 1
)

fun main(args: Array<String>) {
    createDoubleGate(
        name = "AND",
        gate = { x1, x2 -> x1 and x2 },
        functionHeader = "(-1.5+ X1+ X2)",
        function = { x1, x2 -> -1.5 + x1 + x2}
    )

    createDoubleGate(
        name = "OR",
        gate = { x1, x2 -> x1 or x2 },
        functionHeader = "(-0.5 + X1 + X2)",
        function = { x1, x2 -> -0.5 + x1 + x2}
    )

    createSingleGate(
        name = "NOT",
        gate = { x1 -> x1.toBoolean().not().toInt() },
        functionHeader = "(1 - 2 * X1)",
        function = { x1 -> (1 - 2 * x1).toDouble() }
    )

    createDoubleGate(
        name = "XOR",
        gate = { x1, x2 -> x1 xor x2 },
        functionHeader = "(-0,5 + X1 + X2)",
        function = { x1, x2 -> -0.5 + x1 + x2 }
    )

    createDoubleGate(
        name = "XNOR",
        gate = { x1, x2 -> (x1 xor x2).toBoolean().not().toInt() },
        functionHeader = "(-0,5 + X1 + X2)",
        function = { x1, x2 -> -0.5 + x1 + x2 }
    )
}

private fun createDoubleGate(
    name: String,
    gate: (Int, Int) -> Int,
    functionHeader: String,
    function: (Int, Int) -> Double
) {
    val gateValues = mutableListOf<Int>()
    val functionResultValues = mutableListOf<Double>()

    DOUBLE_DATA.forEach { values ->
        val value = gate(values.first, values.second)
        gateValues.add(value)
        val result = function(values.first, values.second)
        functionResultValues.add(result)
    }

    val firstValues = DOUBLE_DATA.map { it.first }
    val secondValues = DOUBLE_DATA.map { it.second }

    val dataFrame = dataFrameOf(
        IntCol(X1_HEADER, firstValues),
        IntCol(X2_HEADER, secondValues),
        IntCol("$X1_HEADER $name $X2_HEADER", gateValues),
        DoubleCol(functionHeader, functionResultValues),
        IntCol(A_HEADER, gateValues.toList())
    )

    println(dataFrame)
}

private fun createSingleGate(name: String, gate: (Int) -> Int, functionHeader: String, function: (Int) -> Double) {
    val gateValues = mutableListOf<Int>()
    val functionResultValues = mutableListOf<Double>()

    SINGLE_DATA.forEach { value ->
        val gateValue = gate(value)
        gateValues.add(gateValue)
        val result = function(value)
        functionResultValues.add(result)
    }

    val dataFrame = dataFrameOf(
        IntCol(X1_HEADER, SINGLE_DATA),
        IntCol("$name $X1_HEADER", gateValues),
        DoubleCol(functionHeader, functionResultValues),
        IntCol(A_HEADER, gateValues.toList())
    )

    println(dataFrame)
}