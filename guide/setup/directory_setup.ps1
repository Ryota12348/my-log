# ルートは現在の場所に直接作る

# フォルダ一覧
$dirs = @(
    "classes-log",
    "exam\regular",
    "exam\gaku-test",
    "exam\benese"
)

foreach ($d in $dirs) {
    New-Item -ItemType Directory -Path $d -Force | Out-Null
}

# classes-log ファイル
$classFiles = @(
    "classes-log\modern-japanese.md",
    "classes-log\classical-japanese.md",
    "classes-log\english-reader.md",
    "classes-log\english-grammar.md",
    "classes-log\math-2.md",
    "classes-log\math-b.md",
    "classes-log\geography.md",
    "classes-log\japanese-history.md",
    "classes-log\economics.md",
    "classes-log\chemistry.md",
    "classes-log\biology.md",
    "classes-log\info.md"
)

# exam ファイル
$examFiles = @(
    "exam\regular\1st-mid.md",
    "exam\regular\1st-final.md",
    "exam\regular\2nd-mid.md",
    "exam\regular\2nd-final.md",
    "exam\regular\3rd-final.md",

    "exam\gaku-test\1st.md",
    "exam\gaku-test\2nd.md",
    "exam\gaku-test\3rd.md",

    "exam\benese\july.md",
    "exam\benese\october.md",
    "exam\benese\february.md"
)

$allFiles = $classFiles + $examFiles

foreach ($f in $allFiles) {
    New-Item -ItemType File -Path $f -Force | Out-Null
}

Write-Host "classes-log と exam 構造を作成しました！"
