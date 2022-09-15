# Developer Notes

When exporting conda environment make sure that all the channels used are added to channels
One can find these channels in the current fastapi.yml
eg conda env export --from-history> fastapi.yml
--from-history is necessary in order to make it easier to succeed in installing on other devices.
