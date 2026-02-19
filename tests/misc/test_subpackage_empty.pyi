from scipy import misc

# ensure there are no 1.14 remnants lefts:
# https://docs.scipy.org/doc/scipy-1.14.1/reference/misc.html

# pyrefly: ignore [missing-attribute]
misc.__all__  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
# pyrefly: ignore [missing-attribute]
misc.ascent  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
# pyrefly: ignore [missing-attribute]
misc.central_diff_weights  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
# pyrefly: ignore [missing-attribute]
misc.derivative  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
# pyrefly: ignore [missing-attribute]
misc.face  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
# pyrefly: ignore [missing-attribute]
misc.electrocardiogram  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

# ensure that the (empty) submodules are not exported

# pyrefly: ignore[implicit-import]
misc.common  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
# pyrefly: ignore[implicit-import]
misc.doccer  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
