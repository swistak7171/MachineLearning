fun Int.toBoolean(): Boolean = (this != 0)

fun Boolean.toInt(): Int = if (this) 1 else 0