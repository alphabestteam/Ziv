@echo off
set output_file=running_pods_list.txt
kubectl get pods --all-namespaces --field-selector=status.phase=Running -o wide > %output_file%
echo DONE
