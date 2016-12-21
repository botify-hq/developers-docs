## Permissions
Describes the list of operations the field can be used for. The rights may include the following:
- **select:** can be used in [[BQLQuery;bql-query]] fields.
- **filters:** can be used in [[BQLFilter;bql-filter]].
- **filters_exist:** can **only** be used with a [[exist predicate;bql-filter#exists-predicate]] in a BQLFilter.
- **sort:** can be used in BQLFilter [[sort;bql-query]].
- **agg:categorical:** can be used in BQLAggsQuery [[groupby;bql-aggs-query#simple-groupby]].
- **agg:numerical:** can be used in BQLAggsQuery [[range groupby;bql-aggs-query#range-groupby]].


## Type
Describes the basic type of the data as it is stored. It defines which [[predicates;bql-filter#predicates]] are available and which type of input to use.
